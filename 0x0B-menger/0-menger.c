#include "menger.h"

/**
 * menger - Function that draws a 2D Menger Sponge
 *
 * @level: (Int) The level of the Menger Sponge to draw
 *
 * Return: None
 */
void menger(int level)
{
	int x, y, _x, _y, size = 1;
	char _print = ' ';

	if (level >= 0)
	{
		for (x = 0; x < level; x++)
		{
			size *= 3;
		}

		for (x = 0; x < size; ++x)
		{
			for (y = 0; y < size; ++y)
			{
				_x = x;
				_y = y;
				_print = '#';

				while (_x && _y)
				{
					if (_x % 3 == 1 && _y % 3 == 1)
					{
						_print = ' ';
						break;
					}

					_x /= 3;
					_y /= 3;
				}
				printf("%c", _print);
			}
			printf("\n");
		}
	}
}
