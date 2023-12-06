#User function Template for python3

class Solution:
    def secFrequent(self, arr, n):
        # code here
        freq_dict = {}
        for word in arr:
            freq_dict[word] = freq_dict.get(word, 0) + 1
    
        # Find the maximum and second maximum frequencies
        max_freq = second_max_freq = float('-inf')
        for count in freq_dict.values():
            if count > max_freq:
                second_max_freq = max_freq
                max_freq = count
            elif count > second_max_freq and count < max_freq:
                second_max_freq = count
    
        # Find the string with the second maximum frequency
        for word, count in freq_dict.items():
            if count == second_max_freq:
                return word
    
        # If no second most frequent string is found
        return ""


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input().strip())
        arr = input().strip().split(" ")
        ob = Solution()
        ans = ob.secFrequent(arr,n)
        print(ans)
# } Driver Code Ends