using Lab_2.HashTable;
// add 30 elements to the HashTable class and print them out
// HashTableWorksForStrings<string> hashTable = new HashTableWorksForStrings<string>();
// hashTable.Add("1", "one");
// hashTable.Add("1", "one");


HashTable<string> hashTable = new HashTable<string>();
hashTable.Add("1", "one");
hashTable.Add("2", "two");
hashTable.Add("3", "three");
hashTable.Add("4", "four");
System.Console.WriteLine(hashTable.Get("1"));
System.Console.WriteLine(hashTable.Get("2"));
System.Console.WriteLine(hashTable.Get("3"));
System.Console.WriteLine(hashTable.Get("4"));
System.Console.WriteLine(hashTable.GetKey("one"));
System.Console.WriteLine(hashTable.GetKey("two"));
System.Console.WriteLine(hashTable.GetKey("three"));
System.Console.WriteLine(hashTable.GetKey("four"));
