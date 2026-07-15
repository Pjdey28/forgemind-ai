class ContextCompressor:

    def compress(

        self,

        context,

        max_documents=5

    ):

        context["documents"] = context["documents"][:max_documents]

        return context