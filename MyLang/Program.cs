using MyLang.HashTable;
using MyLang.Lexer;

internal class Program
{

    private static void TestTable()
    {
        // Set 1
        HashTable<string> hashTable = new HashTable<string>();
        hashTable.Add("1", "one");
        hashTable.Add("2", "two");
        hashTable.Add("3", "three");
        hashTable.Add("4", "four");
        Console.WriteLine(hashTable.Get("1"));
        Console.WriteLine(hashTable.Get("2"));
        Console.WriteLine(hashTable.Get("3"));
        Console.WriteLine(hashTable.Get("4"));
        Console.WriteLine(hashTable.GetKey("one"));
        Console.WriteLine(hashTable.GetKey("two"));
        Console.WriteLine(hashTable.GetKey("three"));
        Console.WriteLine(hashTable.GetKey("four"));

        // Set 2 - The same as above but make the key to be integer
        HashTable<int> hashTable2 = new HashTable<int>();
        hashTable2.Add(1, "one");
        hashTable2.Add(2, "two");
        hashTable2.Add(3, "three");
        hashTable2.Add(4, "four");
        Console.WriteLine(hashTable2.Get(1));
        Console.WriteLine(hashTable2.Get(2));
        Console.WriteLine(hashTable2.Get(3));
        Console.WriteLine(hashTable2.Get(4));
        Console.WriteLine(hashTable2.GetKey("one"));
        Console.WriteLine(hashTable2.GetKey("two"));
        Console.WriteLine(hashTable2.GetKey("three"));
        Console.WriteLine(hashTable2.GetKey("four"));
    }

    private static void Main(string[] args)
    {
        // TestTable();
        Lexer lexer = new Lexer();
        lexer.ReadTokens();
    }
}
