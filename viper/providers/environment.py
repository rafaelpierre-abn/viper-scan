from dataclasses import dataclass, field
import logging
from subprocess import PIPE, run
from typing import List, LiteralString
import re

@dataclass
class EnvironmentProvider:

    command: List[LiteralString] = field(default_factory = lambda: ["pip", "freeze"])


    def preprocess(
        self,
        dependencies: str,
        pattern: str = r"(\S+)==(\S+)"
    ) -> List[dict]:

        result = []
        compiled_pattern = re.compile(pattern)
        matches = compiled_pattern.findall(dependencies)

        for match in matches:
            package_name, package_version = match
            result.append({
                "package": package_name,
                "version": package_version
            })

        return result
        

    def get_dependencies(self) -> List[LiteralString]:

        result = run(
            self.command,
            stdout=PIPE,
            stderr=PIPE,
            universal_newlines=True
        )

        dependencies = self.preprocess(dependencies = result.stdout)
        return dependencies

        