class Codec:
    def encode(self, strs: List[str]) -> str:
        result = []
        
        for string in strs:
            for c in string:
                result.append(str(ord(c)))
                result.append(';')
            result.append(' ')
                
        return ''.join(result)
        

    def decode(self, s: str) -> List[str]:
        result = []
        strings = s.split(' ')
		
        for string in strings:
            temp = []
            for c in string.split(';'):
                if c:
                    temp.append(chr(int(c)))
            result.append(''.join(temp))
			
        result.pop()
        return result


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))