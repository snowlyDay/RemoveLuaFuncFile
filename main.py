# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def check_full_line_code(line):
    lineStack = []
    for code in line:
        if code == '(':
            lineStack.append(code)
        if code == ')':
            popEle = lineStack.pop()
            if popEle != '(':
                lineStack.append(popEle)
    return len(lineStack) == 0


def get_lua_file_content(file, start):
    file_content = ''
    full_log_line = ''
    with open(file, "r") as reader:
        for line in reader:
            pureLine = line.strip()
            if len(full_log_line) > 0:
                if check_full_line_code(full_log_line + line):
                    # print('cur full ' + full_log_line + line)
                    full_log_line = ''
                    continue
                else:
                    full_log_line = full_log_line + line
                    continue
            else:
                if pureLine.startswith(start):
                    if check_full_line_code(line):
                        full_log_line = ''
                        continue
                    else:
                        full_log_line = full_log_line + line
                        continue
            file_content = file_content + line
    with open(file, 'w') as writer:
        writer.write(file_content)


file_path = '/Volumes/Work/program/client/Assets/WGame/Scripts/LuaFramework/Lua/LuaMainLoop.lua'
start_with = 'LogMgr.Log'
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_lua_file_content(file_path, start_with)
    get_lua_file_content(file_path, 'print')
    get_lua_file_content(file_path, 'table.dump')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
