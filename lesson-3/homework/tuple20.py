#Create a new tuple that contains subtuples, where each subtuple contains specified elements from the original tuple.

tuple1=(1,2,3,4,5,6,7,8,9,10)
tuple2=(tuple1[0],tuple1[1],tuple1[2])
tuple3=(tuple1[3],tuple1[4],tuple1[5])
tuple4=(tuple1[6],tuple1[7],tuple1[8])
tuple5=(tuple1[9],)
tuple6=(tuple2,tuple3,tuple4,tuple5)
print(tuple6)
