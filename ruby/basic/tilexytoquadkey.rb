def get_quadkey x, y, lv
	quadkey = ''

	i = lv
	while i > 0 do
		digit = 0
		mask = 1 << (i - 1)
		if (x & mask) != 0
			digit = digit + 1
		end

		if (y & mask) != 0
			digit = digit + 2
		end

		quadkey = quadkey + digit.to_s
		i = i - 1
	end

	quadkey
end

# puts get_quadkey 3,2,4

def get_img_uri_template map_type, app_id
	uri_template = "http://dev.virtualearth.net/REST/v1/Imagery/Metadata/#{map_type}?&incl=ImageryProviders&o=xml&key=#{app_id}"
	uri_template
end

puts get_img_uri_template 'road', 'AhDBjJalvtRXvYe6BsKuj2DwHT9Atlkas7HNVU7rDvoUvIu0_L_GVtSc8y9gNP61'

