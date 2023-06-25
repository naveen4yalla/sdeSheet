class Solution:
    def asteroidCollision(self, asteroids):
        stack = []

        # Iterate over asteroids
        for asteroid in asteroids:
            
            # if stack top is positive and asteroid is negative
            while stack and stack[-1] > 0 and asteroid < 0:

                # if asteroid is greater then remove the current stack top element
                if abs(stack[-1]) < abs(asteroid):
                    stack.pop()
                    continue
                
                # If equal remove top and dont add current asteroid
                elif abs(stack[-1]) == abs(asteroid):
                    stack.pop()
                break

            else:
                stack.append(asteroid)

        # return Stack
        return stack
