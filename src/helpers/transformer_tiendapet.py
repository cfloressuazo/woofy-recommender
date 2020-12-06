"""
Module to cleanup tiendapet dataset from web
"""
import re


class TransformerTiendaPet:
    def __init__(self, raw_data: list[dict]):
        self.raw_data = raw_data

        self.nutritional_facts_lines = self.filter_nutritional_fact_lines()

    def filter_nutritional_fact_lines(self) -> list:
        """"""
        search = re.compile(r'[a-z0-9.]').search
        filtered_lines = []
        for line in self.raw_data:
            if search(''.join(line.get('nutritional_facts', ''))):
                filtered_lines.append(line)
        return filtered_lines

    @staticmethod
    def has_any_digits(string: str) -> bool:
        """"""
        return any(str.isdigit(l) for l in string)

    def filter_protein_lines(self, nutritional_facts_list: list) -> str:
        """"""
        search = re.compile(
            r'prote\wnas?\s(?:\w+\s).*?(?:\()?((?:\d+)(?:.)?(?:\d+.?%))(?:\))?|prote\wnas?:?\s(?:\()?(\d+.?%)(?:\))?|prote\wnas?\s(?:\w+\s?:?).*?((?:\d+)?(?:.)?(?:\d+.?%))|prote\wna?s?:?(?:\\\w+)?\s+(?:\.+)?((?:\d+)(?:.)?(?:\d+.?%))|prote\wna\s(?:\(\w+\)).*?(\d+.?%)',
            re.MULTILINE | re.IGNORECASE | re.UNICODE).search
        p = None
        for _ in nutritional_facts_list:
            result = search(_)
            if result:
                p = ''.join([_ for _ in result.groups() if _])
                break
        search = re.compile(r'\bprote\wna?s?\b(?:\s)?(?:\w+)?', re.MULTILINE | re.IGNORECASE).search
        if not p:
            for idx, _ in enumerate(nutritional_facts_list):
                result = search(_)
                if result:
                    try:
                        if self.has_any_digits(nutritional_facts_list[idx + 3]):
                            p = nutritional_facts_list[idx + 3]
                        elif self.has_any_digits(nutritional_facts_list[idx + 6]):
                            p = nutritional_facts_list[idx + 6]
                        elif self.has_any_digits(nutritional_facts_list[idx + 4]):
                            p = nutritional_facts_list[idx + 4]
                        elif self.has_any_digits(nutritional_facts_list[idx + 2]):
                            p = nutritional_facts_list[idx + 2]
                        elif self.has_any_digits(nutritional_facts_list[idx + 1]):
                            p = nutritional_facts_list[idx + 1]
                    except IndexError:
                        p = None
                    break
        return p
