    if ch in "{[(":
            top.append(ch)
        else:
            if not top:
                return False
            match = stack.pop()
            if ch == ")" and match != "(":
                return False
            if ch == "}" and match != "{":
                return False
            if ch == "]" and match != "[":
                return False