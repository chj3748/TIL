// union-find | programmers 호텔 방 배정
// github.com/chj3748

#include <string>
#include <vector>
#include <map>
#define ll long long
using namespace std;
map<ll, ll> m;
ll findset(ll x)
{
	if (m[x] == 0) return x;
	return m[x] = findset(m[x]);
}

vector<long long> solution(long long k, vector<long long> room_number) {
	vector<long long> answer;
	for (int i = 0; i < room_number.size(); i++)
	{
		ll now = room_number[i];
        ll nowEnd = findset(now);
        m[nowEnd] = nowEnd + 1;
        answer.push_back(nowEnd);

	}
	return answer;
}