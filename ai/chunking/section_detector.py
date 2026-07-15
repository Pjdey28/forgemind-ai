import re


class SectionDetector:

    SECTION_PATTERNS = [

        r"^\d+\.",

        r"^\d+\.\d+",

        r"^[A-Z ]{5,}$",

        r"^WARNING",

        r"^CAUTION",

        r"^NOTE",

        r"^OBSERVATION",

        r"^INSPECTION",

        r"^RECOMMENDATION",

        r"^ROOT CAUSE",

        r"^MAINTENANCE",

        r"^SAFETY"

    ]

    def is_heading(self, line):

        line = line.strip()

        for pattern in self.SECTION_PATTERNS:

            if re.match(pattern, line):

                return True

        return False