#include <iostream>

using namespace std;

int main()
{
    int i;

    const char *oStr = "Holo word!";
    int len = strlen(oStr);

    char *key = new char[len];

    char *shStr = new char[len];

    for (i = 0; i < len; i++)
        key[i] = (char)rand() % 255;

    for (i = 0; i < len; i++)
        shStr[i] = oStr[i] ^ key[i];

    cout << "OPEN TEXT " << oStr << endl;

    cout << "CLOSE TEXT " << shStr << endl;

    return 0;
}