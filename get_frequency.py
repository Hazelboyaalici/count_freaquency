nums=[4,1,2,1,2]

def get_frequency(nums):
  freq={}
  for num in nums:
    freq[num] =freq.get(num,0) +1
  # dict içindeki verilerle oynaka istediğinde get veya default metotlarını kullan ama okumak istediğinde items veya keys kullan.
  #aynı buradaki gibi items kullanırsan hem key hem de value okuyabilirsin
  for number, count in freq.items():
    if count==1: 
      return number

print(get_frequency(nums))
