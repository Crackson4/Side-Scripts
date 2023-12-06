#include <iostream>
#include <vector>

class prime_calculator
{
private:
    /* data */
public:
    std::vector<int> primes;

    prime_calculator(int n)
    {
        this->primes.resize(n);
        calculate_primes(n);
    };

    bool check_prime(int n)
    {
        for (int i = 2; i < n / 2; i++)
        {
            if (n % i == 0)
            {
                return false;
            }
        }

        return true;
    }

    void calculate_primes(int n)
    {
        int count = 0, i = 2;

        while (count < n)
        {
            if (check_prime(i))
            {
                primes[count++] = i;
            }

            i++;
        }
    }

    int get_prime(int n)
    {
        return primes.at(n - 1);
    }

    std::vector<int> get_primes(int n)
    {
        return std::vector<int>(primes.begin(), primes.begin() + n);
    }
};

int main()
{
    int n;

    std::cout << "Enter the amount of primes to be calculated: ";
    std::cin >> n;
    prime_calculator pc(n);

    return 0;
}