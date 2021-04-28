#include <stdio.h>
#include <string.h>
char *reverse(char str1[])   //char *str1
{
    int i,j,c,len=0;
    len=length(str1);
    for(i=0,j=len-1;i<j;i++,j--)
    {
        c=str1[i];
        str1[i]=str1[j];
        str1[j]=c;
    }
    return str1;
}
int length(char *str)   //char str[]
{
    int i,length=0;
    for(i=0;str[i]!='\0';i++)
    {
        length++;
    }
    return length;
}

int main()
{
    char s[50],s1;
    printf("enter a string : ");
    scanf("%s",s);
    s1=reverse(s);
    if(s==s1)
        printf("string is palindrome");
    else
        printf("not palindrome");
    return 0;
}