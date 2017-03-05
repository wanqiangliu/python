#获取国际标准的国别码
from pygal.i18n import COUNTRIES
"""根据指定的国家名,返回pygal使用的两个字母的国别码"""
def get_country_code(country_name):
	for code,name in COUNTRIES.items():
		if name == country_name:
			return code
	return None

if __name__ == "__main__":
	print(get_country_code('United Arab Emirates'))
	print(get_country_code('Andorra'))
	print(get_country_code('China'))