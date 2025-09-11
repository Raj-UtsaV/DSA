// // #include<iostream>
// // using namespace std;

// // int main(){
// // 	int a;
// // 	cin>>a;
// // 	while(a--){
// // 		int b;
// // 		cin>>b;
// // 		string s;
// // 		cin>>s;
// // 		int count  = 0;
// // 		int i = 0;
// // 		while(i<b){
			
// // 			int c = i+4;
// // 			for(int j = i;j<c;j++,i++){
// // 				if((s[i] != 'a') || (s[i] != 'e') || (s[i] != 'i') || (s[i] != 'o') || (s[i] != 'u')){
// // 				count++;
				
// // 				}
				
// // 				}
// // 				i++;
// // 			if(count >= 4 ) {cout<<"NO"<<endl; break;}
// // 			else count = 0;
			
// // 		}
// // 		if(count < 4 ) cout<<"Yes" <<endl;
// // 	}
// // 	return 0;
// // }



#include<iostream>
usign namespace std;

int main(){
	int b;
	cin>>b;
	while(b--){
		int c;
		cin>>c;
		string s;
		cin>>s;
		int count = 0;
		if(s[c-1] == '1'){
			for(int i = 0;i<c-1;i++){
				if(s[i] == 'i') count++;
			}
		}
		else{
			for(int i = 0;i<c;i++){
				if(s[i] == 'i') count++;
			}
		}
		if(count == c) cout<<"0"<<endl;
		else cout<<count<<endl;
	}
	return 0;
}



//1944B
// #include<iostream>
// using namespace std;

// int main(){
// 	int a,b;
// 	cin>>a>>b;
// 	int c = a*2;
// 	int arr[c];
// 	int v= b*4;
// 	int arr1[v];
// 	int l = 0;
	

// 	for(int i=0;i<c;i++){
// 		cin>>arr[i];
// 	}
// 	for(int i = 0;i<c/2;i++){
// 		for(int j = c/2;j<c;j++){
// 			if((arr[i] ^ arr[i+1]) == (arr[j] ^ arr[j+1])) {
				
// 				int p = l;
// 				int k = i;
// 				while(l<p+2){
// 					arr1[l] = arr[k]; 
// 					k++;
// 					l++;
// 				}
// 				int p1 = l;
// 				int k1 = j;
// 				while(l<p1+2){
// 					arr1[l] = arr[k1]; 
// 					k1++;
// 					l++;
// 				}
				
// 			}
				
// 		}
// 	}
// 	for(int i = 0 ; i<v;i++){
// 		cout<<arr1[i]<<" ";
// 	}
// 	return 0;

// }
