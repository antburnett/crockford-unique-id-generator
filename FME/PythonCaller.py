import fme
from fme import BaseTransformer
import fmeobjects
import random

class FeatureProcessor(BaseTransformer):
    """Crockford Base32 ID Generator
    Generates globally unique IDs using Crockford Base32 encoding.
    Perfect for entities requiring short, readable IDs.
    """
    
    def __init__(self, id_length=12):
        """Initialize the Crockford Base32 alphabet and set the ID length."""
        # Crockford Base32: excludes I, L, O, U, 0 for human readability
        self.alphabet = "123456789ABCDEFGHJKMNPQRSTVWXYZ"  # Define the Crockford Base32 alphabet
        self.id_length = id_length  # Set the length of the ID to be generated
        
    def has_support_for(self, support_type: int):
        """Enable bulk mode for performance with large datasets."""
        # Check if the support type matches the feature table shim constant
        return support_type == fmeobjects.FME_SUPPORT_FEATURE_TABLE_SHIM
        
    def generate_crockford_id(self):
        """Generate a Crockford Base32 ID of the specified length."""
        # Create a random ID using the Crockford Base32 alphabet
        return ''.join(random.choice(self.alphabet) for _ in range(self.id_length))
        
    def input(self, feature: fmeobjects.FMEFeature):
        """Process each feature and add the generated ID."""
        # Generate the unique ID
        the_cuid = self.generate_crockford_id()
        
        # Set the generated ID as an attribute on the feature
        feature.setAttribute("_cuid", the_cuid)
        
        # Output the feature with the generated ID
        self.pyoutput(feature, output_tag="PYOUTPUT")
        
    def close(self):
        """Cleanup after all features processed."""
        # No specific cleanup actions required
        pass
        
    def process_group(self):
        """Called when group processing mode is enabled."""
        # No specific group processing actions implemented
        pass
        
    def reject_feature(self, feature: fmeobjects.FMEFeature, code: str, message: str):
        """Output rejected features."""
        # Set rejection code and message as attributes on the feature
        feature.setAttribute("fme_rejection_code", code)
        feature.setAttribute("fme_rejection_message", message)
        
        # Output the rejected feature with a specific tag
        self.pyoutput(feature, output_tag="<Rejected>")