# string replace | programmers 방금그곡
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def replace_a(s):
    s = s.replace('C#', 'c')
    s = s.replace('D#', 'd')
    s = s.replace('F#', 'f')
    s = s.replace('G#', 'g')
    s = s.replace('A#', 'a')
    return s


def solution(m, musicinfos):
    m = replace_a(m)
    l = len(m)

    def new_musicinfo(info):
        info_split = info.split(',')
        start_h, start_m = map(int, info_split[0].split(':'))
        end_h, end_m = map(int, info_split[1].split(':'))
        t = (end_m + 60 * (end_h - start_h)) - start_m
        info = replace_a(info_split[3])
        return [t, info_split[2], info]

    musicinfos = sorted(list(map(new_musicinfo, musicinfos)), key=lambda x: -x[0])
    for t, music_name, info in musicinfos:
        music_l = len(info)
        mul = (l // music_l) + 1
        check_info = info[:t] if t <= music_l else info * (mul + 1)
        if l > t:
            continue
        if m in check_info:
            return music_name
    return "(None)"