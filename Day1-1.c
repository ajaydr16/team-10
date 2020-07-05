#include<stdio.h>
#include<stdlib.h>
#include<malloc.h>

struct node
{
	int data;
	struct node * next;
};

struct node *head=NULL;
struct node *tmp1=NULL;
void insert_first()
{
	int item;
	printf("Please enter a number for insert at first \n ");
	scanf("%d",&item);
	if(head==NULL)
	{
		head=(struct node*) malloc(sizeof(struct node));
		head->data=item;
		head->next=NULL;
		printf("Element is Insterted at first \n");
	}
	else
	{ 
	    struct node *newnode;
		newnode=(struct node*)malloc(sizeof(struct node));
		newnode->data=item;
		newnode->next=head;
		head=newnode;
		printf("Element is Insterted at first \n");
	}
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
		printf("Element is Insterted at last \n");
	}
}


void insert_position()
{
	int pos,item, k=0;
	printf("Enter position for insertion \n");
	scanf("%d",&pos);
	printf("Enter an element \n");
	scanf("%d",&item);
	struct node *newnode;
	newnode=(struct node*)malloc(sizeof(struct node));
	newnode->data=item;
	struct node *tmp,*prev;
	tmp=head;
	if(pos==1)
	{
		newnode->next=tmp;
		head=newnode;
	}
	else
	{
		while((tmp!=NULL)&&(k<pos-1))
		{
			k++;
			prev=tmp;
			tmp=tmp->next;
			
		}
		if(tmp==NULL)
		{
			prev->next=newnode;
			newnode->next=NULL;
		}
		else
		{
			prev->next=newnode;
			newnode->next=tmp;
		}
	}
}



void delete_first()
{
	if(head==NULL)
	{
		printf(" No elements are in the List \n ");
	}
	else
	{
	struct node *tmp=head->next;
    printf(" Deleted element is %d \n",head->data);
	free(head);
	head=tmp;
	}
}
void delete_last()
{
	  if(head==NULL)  
	{
		printf(" No elements are in the List \n ");
	}
	else
	{	
		if(head->next==NULL) 
		{
			printf(" Deleted element is %d \n",head->data);
			free(head);
			head=NULL;
   	    }
	   else
	   {	   
	   		struct node *tmp=head,*prev=head;
	   		while(tmp->next!=NULL) 
			{
				prev=tmp;
				tmp=tmp->next;
			}
				printf(" Deleted element is %d\n",tmp->data);
			free(tmp);
			prev->next=NULL;	
		}
   }
}

void delete_position()
{
	int pos,item, k=0;
	printf("Enter position for deletion \n");
	scanf("%d",&pos);
	struct node *tmp,*prev;
	tmp=head;
	if(head==NULL)
	{
		printf("List is Empty \n");
		return;
	}
	if(pos==1)
	{
		
			head=head->next;
			free(tmp);
			return;
	}
	else 
	{
		while((tmp!=NULL)&&(k<pos-1))
		{
			k++;
			prev=tmp;
			tmp=tmp->next;
			
		}
		if(tmp==NULL)
		{
			printf("Position does not exists \n");
		}
		else
		{
			prev->next=tmp->next;
			free(tmp);
		}
	}
}

void traverse()
{
	if(head==NULL)
	{
		printf("List is Empty \n");
		return;
	}
	else
	{
		struct node *tmp;
		tmp=head;
			printf("\nThe Updated Single Linked List is : ");
		while(tmp!=NULL)
		{
			
			printf("%d -> ",tmp->data);
			tmp=tmp->next;
		}
		
	}
}
int search_rec(struct node *tmp, int ele){
	if (tmp == NULL) 
        return 0; 
    if (tmp->data == ele) 
        return 1; 

    return search_rec(tmp->next,ele); 
}
void search(){
	int ele;
	printf("Enter an element to search\n");
	scanf("%d",&ele);
	if(search_rec(head,ele)==1)
		printf("Element found\n");
	else
		printf("Element not found\n");	
	
}
void main()
{
	int choice;

	while(1)
	{
	printf("\n--------------------------\nEnter your option: \n1. Insert at first  \n2. Insert at last \n3. Insert at given postion \n4. Delete at first \n5. Delete at last \n6. Delete at given position \n7. Searching Element \n8. Traversing \n9. Exit \n ----------------------\n ");
	scanf("%d",&choice);
	
		switch(choice)
		{
			case 1: 
				 insert_first();
				  traverse(); 
			 	 break;
			case 2: 
			 	  insert_last();
			 	   traverse(); 
			 	 break;
		 	case 3:
				insert_position();
				 traverse(); 
		 		 break;
			case 4: 
				delete_first();
				 traverse(); 
				break;
			case 5: 
				delete_last();
				 traverse(); 
				break;
			case 6:
				delete_position();
				 traverse(); 
				 break;
			case 7: 
				 search(); 
		   	 	break;
		   	case 8:
		   		 traverse(); 
				   break;
			case 9:
				 exit(1);
			default: 
			      printf(" Invalid Choice \n");
		}
	}
	
}
