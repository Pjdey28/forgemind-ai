class SemanticRetriever:

    def __init__(

        self,

        repository

    ):

        self.repository = repository

    def retrieve(

        self,

        embedding,

        filters,

        top_k=5

    ):

        return self.repository.search(

            embedding,

            filters,

            top_k

        )