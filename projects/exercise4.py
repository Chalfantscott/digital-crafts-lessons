total = raw_input("What is the total?")
qualityOfService = raw_input("How was the quality of service?")
if qualityOfService == "good":
    result1 = float(.20 * float(total)) 
    print result1
elif qualityOfService == "fair":
    print float(.15 * float(total)) 
elif qualityOfService == "bad":
    print float(.10 * float(total))
split = raw_input("how many people are splitting the bill?")

print result2(float(total) * float(qualityOfService)) 
