#User function Template for python3

class Solution:
    def asteroidCollision(self, N, asteroids):
        # Code here
        stack = []

        for asteroid in asteroids:
            # While there are asteroids moving left and the current asteroid is moving right
            while stack and stack[-1] > 0 and asteroid < 0:
                # Check the absolute values to determine which asteroid will explode
                if abs(stack[-1]) == abs(asteroid):
                    stack.pop()
                    break
                elif abs(stack[-1]) > abs(asteroid):
                    break
                else:
                    stack.pop()
            else:
                # If no collision or the current asteroid survives the collision, add it to the stack
                stack.append(asteroid)

        return stack


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        asteroids = list(map(int, input().split()))
        ob = Solution()
        res = ob.asteroidCollision(N, asteroids)
        for val in res:
            print(val, end = ' ')
        print()
# } Driver Code Ends