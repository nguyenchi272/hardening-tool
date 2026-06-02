class FileReplaceHandler:

    def execute(
        self,
        collector,
        fix_data
    ):

        file = fix_data["file"]

        search = fix_data["search"]

        replace = fix_data["replace"]

        command = f"""
sed -i 's/{search}/{replace}/g' {file}
"""

        return collector.run_command(

            command,

            sudo=True
        )