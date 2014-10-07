from rest_framework import serializers

class StdImageField(serializers.ImageField):
    """
    Get all the variations of the StdImageField
    """
    def to_native(self, obj):
        return self.get_variations_urls(obj)

    def get_variations_urls(self, obj):
    	""" 
    	Get all the logo urls.
    	"""

    	# Initiate return object
    	return_object = {};

    	# Get the field of the object
    	field = obj.field

    	# A lot of ifs going araound, first check if it has the field variations
    	if hasattr(field, 'variations'):
    		# Get the variations
    		variations = field.variations
    		# Go through the variations dict
    		for key, attr in variations.iteritems():
    			# Just to be sure if the stdimage object has it stored in the obj
    			if hasattr(obj, key):
    				# get the by stdimage properties
    				fieldObj = getattr(obj, key, None)
    				if fieldObj:
    					# Check if there is an url
    					url = getattr(fieldObj, 'url', None)
            			if url:
            				#store it, with the name of the variation type into our return object
            				return_object[key] = url
        
        # Also include the original (if possible)
        if hasattr(obj, 'url'):
        	return_object['original'] = obj.url

        return return_object


    def from_native(self, data):
    	""" Just go with the flow """
        return super(serializers.ImageField, self).from_native(data)
	