class Solution:
    def sort012(self, arr):
        z, o, t = [], [], []

        for i in arr:
            if i == 0:
                z.append(i)
            elif i == 1:
                o.append(i)
            else:
                t.append(i)

        idx = 0
        
        for x in z:
            arr[idx] = x
            idx += 1

        for x in o:
            arr[idx] = x
            idx += 1

        for x in t:
            arr[idx] = x
            idx += 1
        return arr    
        
