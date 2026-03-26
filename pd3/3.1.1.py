manufacturers = ['A', 'G', 'K', 'N', 'P', 'Q', 'R']

manuNames = ['American Home Food Products: ',
             'General Mills: ',
             'Kelloggs: ',
             'Nabisco: ',
             'Post: ',
             'Quaker Oats: ',
             'Ralston Purina: ']


handle = open(input('Enter file: '), 'r')

descriptors = None
x = 0

current_type = None
cold_max_rating = 0
cold_min_rating = 500
cold_avg_rating = 0
cold_num_rated = 0


cold_max_rated = None
cold_min_rated = None

hot_max_rating = 0
hot_min_rating = 500
hot_avg_rating = 0
hot_num_rated = 0


hot_max_rated = None
hot_min_rated = None

for line in handle:
    if x == 0:
        descriptors = line.split(',')

    if(x > 1): #check if second line
        separated = line.split(',')

        offset = 0
        found = False

        name = separated[0]
        manuIndex = 0

        while(not found): # some names contain commas, use known manufacturer types to find offset
            curr = separated[offset + 1]
            try:
                manuIndex = manufacturers.index(curr)
                found = True
            except:
                name +=',' + curr
                offset += 1
        
        name = name.replace('_', ' ')

        #print(descriptors)

        #print(manuNames[manuIndex] + name)

        rating = float(separated[descriptors.index('rating\n') + offset])

        if(separated[descriptors.index('type') + offset] == 'C'):

            if(cold_max_rating < rating):
                cold_max_rating = rating
                cold_max_rated = name
            
            if(cold_min_rating > rating):
                cold_min_rating = rating
                cold_min_rated = name
            
            cold_avg_rating += rating
            cold_num_rated += 1
        
        else:

            if(hot_max_rating < rating):
                hot_max_rating = rating
                hot_max_rated = name
            
            if(hot_min_rating > rating):
                hot_min_rating = rating
                hot_min_rated = name
            
            hot_avg_rating += rating
            hot_num_rated += 1
    
    x += 1


print('Cereal type: hot')
print('Average rating: ' + str(hot_avg_rating / hot_num_rated))
print('max rated: ' + str(hot_max_rated) + ', with rating of ' + str(hot_max_rating))
print('min rated: ' + str(hot_min_rated) + ', with rating of ' + str(hot_min_rating))

    
print('Cereal type: cold')
print('Average rating: ' + str(cold_avg_rating / cold_num_rated))
print('max rated: ' + str(cold_max_rated) + ', with rating of ' + str(cold_max_rating))
print('min rated: ' + str(cold_min_rated) + ', with rating of ' + str(cold_min_rating))
