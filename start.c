#include <stdlib.h>
#include <stdio.h>
#include <string.h>

char* concat(char *s1, char *s2)
{

    size_t len1 = strlen(s1);
    size_t len2 = strlen(s2);                      

    char *result = malloc(len1 + len2 + 1);

    if (!result) {
        fprintf(stderr, "malloc() failed: insufficient memory!\n");
        return NULL;
    }

    memcpy(result, s1, len1);
    memcpy(result + len1, s2, len2 + 1);    

    return result;
}

int main(int argc, char *argv[])
{
	printf("%d",argc);
	if (argc == 1)
	{
		system("python3 aplfh.py");
		return 0;
	}
	char *s = concat("python3 aplfh.py ", argv[1]);
	system(s);
	return 0;
}
