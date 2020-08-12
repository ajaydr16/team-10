#include<stdio.h>
#include<stdlib.h>
#include<malloc.h>

struct node
{
	int data;
	struct node * next;
};
struct node *head=NULL;

void position()
{
	int pos,item, k=0;
	printf("Enter position:\n");
	scanf("%d",&pos);
	struct node *tmp=head;
	
	
	if(pos==1)
	{
		return;
	}
	else 
	{
		while((tmp!=NULL)&&(k<pos-1))
		{
			k++;
			tmp=tmp->next;
			
		}
		struct node *temp=tmp;
		
		while(tmp->next!=NULL)
			tmp=tmp->next;
		tmp->next=head;
		head=temp->next;
		temp->next=NULL;
		
		
		
	}
	return;
}


int insert()
{
	int item;
	printf("Enter a number to insert or enter '-1' to quit insertion:  \n ");
	scanf("%d",&item);
	if (item==-1){
		return 1;
	}
	if(head==NULL)
	{
		head=(struct node*) malloc(sizeof(struct node));
		head->data=item;
		head->next=NULL;
		printf("Element is Inserted at first \n");
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
		printf("Element is Insterted.\n");
	}
	return insert();
}
int traverse(head){
	struct node *t;
	t=head;
	if(t==NULL){
		return 1;
	}
	printf("%d -> ",t->data);;
	return traverse(t->next);
}
void main(){
	int choice;
	while(1)
	{
	printf("\n--------------------------\nEnter your option: \n1. Insert at first  \n2. Traverse \n3.Position to enter\n4.Exit  \n ----------------------\n ");
	scanf("%d",&choice);
	switch(choice)
		{
			case 1: 
				 insert();
			 	 break;
			case 2: 
			 	   traverse(head); 
			 	 break;
			case 3:
				position();
				break;
			case 4:
				exit(1);
			default:
				printf(" Invalid Choice \n");
		}
	}
}
