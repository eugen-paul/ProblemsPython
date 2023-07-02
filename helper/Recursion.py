def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = stack.append(f(*args, **kwargs))
            while True:
                try:
                    to = stack.append(stack[-1].send(to))
                except StopIteration as e:
                    stack.pop()
                    to = e.value
                    if not stack:
                        break
            return to

    return wrappedfunc


@bootstrap
def dfs(x) -> int:
    if x == 0:
        return 0
    return x + (yield dfs(x-1))


if __name__ == "__main__":
    for i in range(10):
        print(dfs(i))
