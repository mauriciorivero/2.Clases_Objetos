class Libro:
    """
    Clase que representa un libro en una biblioteca.
    
    Attributes:
        title (str): El título del libro
        isbn (str): El código ISBN único del libro (puede usarse como identificador)
        author (str): El nombre del autor del libro
        publication_year (int): El año en que se publicó el libro
        total_num_pages (int): El número exacto de páginas totales del libro
        is_available (bool): El estado del libro, si está prestado o disponible
    """
    
    def __init__(self, title, isbn, author, year, num_pages, available):
        """
        Inicializa una nueva instancia de Libro.
        
        Args:
            title (str): El título del libro
            isbn (str): El código ISBN único del libro
            author (str): El nombre del autor del libro
            year (int): El año de publicación
            num_pages (int): El número total de páginas
            available (bool): Estado de disponibilidad
        """
        self.__title = title
        self.__isbn = isbn
        self.__author = author
        self.__publication_year = year
        self.__total_num_pages = num_pages
        self.__is_available = available
    
    # Propiedades (getters y setters)
    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, title):
        self.__title = title
    
    @property
    def isbn(self):
        return self.__isbn
    
    @isbn.setter
    def isbn(self, isbn):
        self.__isbn = isbn
    
    @property
    def author(self):
        return self.__author
    
    @author.setter
    def author(self, author):
        self.__author = author
    
    @property
    def publication_year(self):
        return self.__publication_year
    
    @publication_year.setter
    def publication_year(self, year):
        self.__publication_year = year
    
    @property
    def total_num_pages(self):
        return self.__total_num_pages
    
    @total_num_pages.setter
    def total_num_pages(self, num_pages):
        self.__total_num_pages = num_pages
    
    @property
    def is_available(self):
        return self.__is_available
    
    @is_available.setter
    def is_available(self, available):
        self.__is_available = available
    
    # Métodos
    def loan(self):
        """Marca el libro como prestado."""
        self.__is_available = False
    
    def return_book(self):
        """Marca el libro como devuelto y disponible."""
        self.__is_available = True