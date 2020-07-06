#include<stdio.h>
#include<stdlib.h>
#include<malloc.h>


struct node
{
	int data;
	struct node * next;
};

struct node *head=NULL;

int fun(){
	int item=0;
	struct node *slow,*fast,*prev;
	slow=fast=head;
	//scanf("%d",&item);
	while(slow && fast && fast->next)
		{
		
		prev=slow;
		slow=slow->next;
		fast=fast->next->next;
		if (slow==fast)
			return 1;
		}
	
	return 0;
	
}
void insert_last()
{
	int item;
	printf("Please enter a number to insert at last \n ");
	scanf("%d",&item);
	if(head==NULL)
	{
		head=(struct node*) malloc(sizeof(struct node));
		head->data=item;
		head->next=NULL;
	}
	else
	{ 
	    struct node *tmp=head;
		while(tmp->next!=NULL)
		tmp=tmp->next;
		struct node *newnode;
		newnode=(struct node*)malloc(sizeof(struct node));
		newnode->data=item;
		newnode->next=NULL;
		tmp->next=newnode;
		//printf("Element is Insterted at last \n");
	}
}
void main()
{
	int count;
	printf("Enter the no. of elements:\n");
	scanf("%d",&count);
	while(count>0){
		insert_last();
		count--;
		
	}
	printf("Checking whether loop exist or not.\n");
	if(fun())
					printf("Loop Exist");
	else
					printf("Loop not Exist");
	
	
	
}
	
