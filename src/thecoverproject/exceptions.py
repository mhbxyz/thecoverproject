
class UnknownRegionError(Exception):

    def __init__(self, region_code):
        self.region_code = region_code
        super().__init__(f"Region code {region_code} is not referenced in region database.")
