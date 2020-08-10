#include<stdio.h>
#include<stdlib.h>
#include<malloc.h>

struct node
{
	int data;
	struct node * next;
};
struct node *head=NULL;


int insert_first()
{
	int item;
	printf("Enter a number to insert or enter '-1' to quit insertion:  \n ");
	scanf("%d",&item);
	if (item==-1)
		return 1;
	if(head==NULL)
	{
		head=(struct node*) malloc(sizeof(struct node));
		head->data=item;
		head->next=NULL;
		printf("Element is Inserted at first \n");
	}
	else
	{ 
	    struct node *newnode;
		newnode=(struct node*)malloc(sizeof(struct node));
		newnode->data=item;
		newnode->next=head;
		head=newnode;
		printf("Element is Inserted at first \n");
	}
	return insert_first();
}
void traverse(head){
	struct node *temp;
	temp=head;
	if(temp==NULL){
		return 1;
	}
	printf("%d -> ",temp->data);;
	return traverse(temp->next);
}
void main(){
	int choice;
	while(1)
	{
	printf("\n--------------------------\nEnter your option: \n1. Insert at first  \n2. Traverse \n3.Quit  \n ----------------------\n ");
	scanf("%d",&choice);
	switch(choice)
		{
			case 1: 
				 insert_first();
			 	 break;
			case 2: 
			 	   traverse(head); 
			 	 break;
			case 3:
				exit(1);
			default:
				printf(" Invalid Choice \n");
		}
	}
}
