#! /usr/bin/env python
#coding:utf-8

def divide(numerator, denominator, detect_repetition=True, digit_limit=None):

    # 如果是无限小数，必须输入限制的返回小数位数:digit_limit
    # digit_limit = 5，表示小数位数5位，注意这里的小数位数是截取，不是四舍五入.
    if not detect_repetition and digit_limit == None:
        return None

    decimal_found = False
                                
    v = numerator // denominator
    numerator = 10 * (numerator - v * denominator)
    answer = str(v)
                                                
    if numerator == 0:
        return answer
                                                              
    answer += '.'
    
    # Maintain a list of all the intermediate numerators
    # and the length of the output at the point where that
    # numerator was encountered. If you encounter the same
    # numerator again, then the decimal repeats itself from
    # the last index that numerator was encountered at.
    states = {}
    
    while numerator > 0 and (digit_limit == None or digit_limit > 0):
        
        if detect_repetition:
            prev_state = states.get(numerator, None)
            if prev_state != None:
                start_repeat_index = prev_state
                non_repeating = answer[:start_repeat_index]
                repeating = answer[start_repeat_index:]
                return non_repeating + '[' + repeating + ']'
            states[numerator] = len(answer)

        v = numerator // denominator
        answer += str(v)
        numerator -= v * denominator
        numerator *= 10
        if digit_limit != None:
            digit_limit -= 1
            
            
    if numerator > 0:
        return answer + '...'
    return answer

if __name__=="__main__":
    print "5divide2",
    print divide(5,2)
    print "10divide3",
    print divide(10,3)
    print divide(10,3,5)
    print "15divide7"
    print divide(15,7)
    print divide(15,7,True,3)
    
