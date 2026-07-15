class GraphRetriever:

    def __init__(

        self,

        repository

    ):

        self.repository = repository

    def retrieve(

        self,

        entities,

        depth=2

    ):

        return self.repository.expand(

            entities,

            depth

        )