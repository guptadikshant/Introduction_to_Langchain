FEW_SHOT_EXAMPLE = [
    {
        "travel_query": "Can you plan a trip from Shahdara, Delhi to London?",
        "travel_response": """
        Since this is a international travel request, let's understand the process of travelling from one country to another.
        First we have to book a flight which might have some layover in between and might be a direct flight.To book a flight you can 
        use any of the online service provider. 
        
        The layover options are: Gulf Air flight number GF 131, layover of 3hrs 25 mins at Bahrain and then to destination London-Heathrow Apt.
        Total  cost will be Rs. 28343 per person.

        The direct options are: Vistra flight UK 17 has total cost Rs. 67225, British Airways BA 142 has total cost Rs. 69891

        Now, to reach airport to pick the flight, we need to either travel via Cab/Metro/Train/Buses. The nearest Airport for delhi is Indira 
        Gandhi International Airport (IGI)
        Now there are no direct Train which goes to Delhi's airport.
        So we have left with either Cab/Metro/Buses.
        
        The cab can be booked via Uber/Ola/Private Taxis. The fare will be Rs 600 to Rs 800 and will directly dropped to destination.
        
        The nearest metro station near Shahdara, Delhi is Shahadara Metro station. You have to change metro from Shahdara to Kashmere Gate then 
        from Kashmere Gate to New Delhi and from New Delhi to Terminal-3 via Airport Metro line. This change of station is required because there
        is no direct metro from Shahdara, Delhi to Airport. Total cost is Rs. 45.

        For buses you can make use of Delhi Transport Corporation(DTC) which only runs in Delhi NCR(National Capital Region).
        The buses run every 20 mins and some buses are 717, 717B. It is good you confirm first which bus run on your flight day.
        The cost of fare will Rs. 70 and will take 45 mins.        
        The nearest bus station is IFFCO Chowk which you can reach by Metro but you have first board from Shahdara and then from Shahdara to
        Kashmere gate then from Kashmere gate to IFFCO Chowk. But this route is completely opposite and will take lots of unnecessary time.
        This route will be suitable for those who lives near to IFFCO Chowk.

        The most economical and convenient option is Metro if you have less luggage but if you have more luggage and more people, I suggest to go
        via Cab to Airport.

        """ 
    },
    {
        "travel_query": "Plan a trip from South Goa to Gorakhpur, Uttarpradesh?",
        "travel_response": """
        Since this is a domestic travel request, let's understand the process of travelling from one city to another city. 
        First we have to book the mode of transport which we need to travel from source to destination. It might be flight/train/cab/buses.
        But for this request there are no direct buses available from South Goa to Gorakhpur.

        We need to suggest nearest Airport/Train Station to customer. If not available suggest the next nearest, and the way to reach there.

        There are no direct flights from South Goa to Gorakhpur. 
        IndiGo flight number 6E 744 will first fly from Goa to Hyderabad which has layover of 2hrs 40 mins and then from Hyderabad to Gorakhpur.
        The nearest airport from South Goa is GOI, Goa and nearest airport from Gorakhpur is GOP. The total cost will be Rs. 15624.

        To reach GOI airport you can make use of Cabs which will cost around Rs. 2500. There are no Ola/Uber in Goa, so you have to use private
        cabs only.

        For Train, you can book 04095-Madgaon Hazrat Nizamuddin Winter AC Special which starts from KRMI, Goa at 07:18 PM and reach
        to Basti Station at 12:32 AM. The journey has 20 stops and covers 1558 KM. Total cost will be between Rs. 1200 to Rs. 5500

        """
    },
    {
        "travel_query": "Can you plan a trip from Juhu, Mumbai to New York, U.S.A.?",
        "travel_response": """
        This is a international travel request.
        First we have to book a flight which might have some layover in between and might be a direct flight. 

        Emirates flight number Ek-509 from Chatrapati Shivaji Airport, Terminal-2, stops at Dubai International Airport 
        for a layover of 9hrs 25 mins and then to John F Kennedy Airport, Terminal-4. Total cost Rs. 63264.

        Air India flight number AI-119 departs from  Chatrapati Shivaji Airport, Terminal-2 and arrives directly at John F Kennedy Airport.
        Total cost will be Rs. 98406.

        Nearest Airport from Juhu Beach is Chhatrapati Shivaji Maharaj International Airport. To reach there, we either need 
        taxi/train/cab/buses/autos.
        Cabs can be booked from Uber/Ola having an average fare of Rs. 280. Autos will have Rs 21. 

        Nearest Metro station is Sakinaka which is 29 mins walk away. Cost would be Rs. 30

        To travel from Juhu Beach to Chhatrapati Shivaji Maharaj International Airport, you can take a train from Vile Parle railway 
        station to Santacruz Station, which takes approximately 34 minutes and operates every 30 minutes. 
        Alternatively, you can take a bus from Mumbai CST to Juhu Beach, which costs $1 and takes 1h 9m. 
        The nearest railway station to Juhu Beach is the Vile Parle railway station, which is about 3 km away. 
        The Chhatrapati Shivaji Maharaj International Airport is only 2.8 Km away from the Vile Parle railway station, 
        making it easy to find local transport options to cover the distance between the station and the airport.

        
        """
    }
]