#include <stdio.h>
#include <stdlib.h>


typedef struct node
{
    int data;// this will store data.
    struct node *next;//this will store address of that data
}node;

node *createLinkedlist(int);
void displinklist(node *);
int main()
{
    int n;
    node *HEAD=NULL;// WE NEED TO COLLECT ALL THE head ADDERSS that will come
    printf("enter the number of nodes");
    scanf("%d",&n);
    HEAD=createLinkedlist(n);
    displinklist(HEAD);
}

node *createLinkedlist(int n)
{
    int i=0;
    node *head=NULL;// head is a pointer
    node *temp=NULL;//temp node
    node *p=NULL;//adding the node
    for(i=0;i<n;i++)
    {
        /*

        TO CREATE AN ISOLATED NODE

        */
        temp=(node*)malloc(sizeof(node));//this malloc return void * or void address so (node*) is used to convert address
        printf("enter the value of node");
        scanf("%d",&(temp->data));// data will be in data
        temp->next=NULL;
        //till process will create an isolated node only
        if(head==NULL)//when loop run first time
        {
            head=temp;// if list is empty then make temp as first node is temp
        }
        else//23->65->90-> NULL     98->NULL
        {
            p=head;
            while(p->next!=NULL)//p will till 90
            {
                p=p->next;
            }
            p->next=temp;//we will assign next place to p as 98
        }
    }
    return head;
}
void displinklist(node *head)
{
    node *p=head;
    while(p!=NULL)
    {
        printf("%d->",p->data);
        p=p->next;
    }//21->55->41->65-> first p will go to 21 then it will move to 55 by using p->next
 }
