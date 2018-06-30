#include <iostream>
#include<cmath>
int main()

{
	int n, m;
	std::cin >> n >> m;
	int temp = (n - m)/2;
	//std::abs(temp)

	for (int i = 1; i <=n; i++)
	{
		for (int j = 1; j <= n; j++)
		{
			if (((j > temp) && (j <= n - temp))||((i>temp)&&(i<=n-temp)))
			{
				std::cout << "*";
			}
			else
			{
				std::cout << " ";
			}
		}
		std::cout << "\n";
	}

}
