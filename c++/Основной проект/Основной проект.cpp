#include <iostream>
#include <cstring>
#include <cmath>
#include <Windows.h>
using namespace std;

// 1 
float addarrays(float a1, float a2) {
	float a3;
	a3 = a1 + a2;
	return a3;
}
// 1

// 2
int compstr(char* str1, char* str2) {
	while (*str1 and *str2 and (*str1 == *str2)) {
		str1++;
		str2++;
	}
	if (*str1 > *str2) {
		return 1;
	}
	if (*str1 < *str2) {
		return -1;
	}
	return 0;

}
// 2

// 3
/////////
// 3

// 4
/////////
// 4

// 5
struct person
{
	char* name1;
	int zp;

	void input() {
		SetConsoleCP(1251);
		char* name = new char[20];
		cout << "Введите имя работника: ";
		cin >> name;
		name1 = name;
		cout << "Введите оклад работника: ";
		cin >> zp;
	}
	void output() {
		SetConsoleOutputCP(1251);
		setlocale(LC_ALL, "ru");
		cout << endl;
		cout << "Имя работника: ";
		cout << name1 << endl;
		cout << "Оклад работника: ";
		cout << zp << endl;
	}
};
void swap(person** arrp, int n) {
	while (n--) {
		bool swapped = false;
		for (int i = 0; i < n; i++) {
			if (arrp[i]->zp > arrp[i + 1]->zp) {
				swap(arrp[i]->zp, arrp[i + 1]->zp);
				char* sw_name = arrp[i]->name1;
				arrp[i]->name1 = arrp[i + 1]->name1;
				arrp[i + 1]->name1 = sw_name;
				swapped = true;
			}
		}
		if (swapped == false) {
			break;
		}
	}
};
// 5

int main() {
	setlocale(LC_ALL, "rus");
	int task = 0;
	for (int i = 0; i < 5; i++) {
		cout << "Введите номер задания (1-5): ";
		cin >> task;
		if (task == 1)
		{
			setlocale(LC_ALL, "ru");
			float array1[5], array2[5], array3[5];
			float a1, a2;

			for (int i = 0; i < 5; i++) {
				cout << "Введите " << i + 1 << "-й из 5 элементов 1-го массива: ";
				cin >> *(array1 + i);
			}

			for (int n = 0; n < 5; n++) {
				cout << "Введите " << n + 1 << "-й из 5 элементов 2-го массива: ";
				cin >> *(array2 + n);
			}

			for (int i = 0; i < 5; i++) {
				float sum;
				a1 = *(array1 + i);
				a2 = *(array2 + i);
				sum = addarrays(a1, a2);
				*(array3 + i) = sum;
			}

			for (int k = 0; k < 5; k++) {
				cout << endl << k + 1 << "-я сумма элементов массивов равна: " << *(array3 + k);
				cout << endl;
			}
		}
		if (task == 2)
		{
			SetConsoleOutputCP(1251);

			char st1[50], st2[50];
			int a, b;

			cout << "Введите первое слово: ";
			cin >> st1;
			cout << "Введите второе слово: ";
			cin >> st2;
			cout << "-1 - первое слово идет первым по алфавиту" << endl;
			cout << "0 - оба слова равнозначны в расстановке по алфавиту" << endl;
			cout << "1 - второе слово идет первым по алфавиту" << endl;

			char* ptr1 = st1, * ptr2 = st2;

			b = compstr(ptr1, ptr2);

			cout << b << endl;
		}
		if (task == 3)
		{
			int* ap[10];
			int a0[10], a1[10], a2[10], a3[10], a4[10], a5[10], a6[10], a7[10], a8[10], a9[10];
			ap[0] = a0;
			ap[1] = a1;
			ap[2] = a2;
			ap[3] = a3;
			ap[4] = a4;
			ap[5] = a5;
			ap[6] = a6;
			ap[7] = a7;
			ap[8] = a8;
			ap[9] = a9;
			for (int i = 0; i < 10; i++) {
				for (int k = 0; k < 10; k++) {
					ap[i][k] = k * 10;
				}
			}
			for (int i = 0; i < 10; i++) {
				for (int k = 0; k < 10; k++) {
					cout << ap[i][k] << ' ';
				}
				cout << endl;
			}
		}
		if (task == 4)
		{
			int* ap[10];

			for (int j = 0; j < 10; j++) {
				*(ap + j) = new int[10];
			}

			for (int j = 0; j < 10; j++) {
				for (int k = 0; k < 10; k++) {
					*(*(ap + j) + k) = k * 10;
				}
			}

			for (int j = 0; j < 10; j++) {
				for (int k = 0; k < 10; k++) {
					cout << *(*(ap + j) + k) << ' ';
				}
				cout << endl;
			}
		}
		if (task == 5)
		{
				SetConsoleOutputCP(1251);
				person* arrp[5];
				for (int j = 0; j < 5; j++) {
					*(arrp + j) = new person;
					arrp[j]->input();
				}
				swap(arrp, 5);
				for (int j = 0; j < 5; j++) {
					arrp[j]->output();
				}
		}
	}
	return 0;
}


