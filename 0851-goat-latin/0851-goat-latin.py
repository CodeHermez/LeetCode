class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        words = sentence.split()
        count = 1
        result = []
        print(words)
        for x in words:
            print('i'==x[0])
            if x[0].lower() == 'a'or x[0].lower() == 'e' or x[0].lower() == 'i' or x[0].lower() == 'o' or x[0].lower() == 'u':
                result.append(x + 'ma'+('a'*count))
                print('jump here')
            else:
                 result.append(x[1:len(x)]+x[0]+'ma'+('a'*count))
            print(' '.join(result))
            count+=1
                
        return ' '.join(result)