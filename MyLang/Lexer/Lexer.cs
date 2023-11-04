using MyLang.HashTable;

namespace MyLang.Lexer
{
    public class Lexer
    {
        private HashTable<int> SymbolTree = new();
        private string[] Letters = new string[52];
        private string[] Digits = new string[10];
        private string[] Operators = new string[9];
        private string[] Separators = new string[11];
        private static string TokenFile = @"Utils\Token.in";
        public void ReadTokens()
        {
            string[] lines = File.ReadAllLines(TokenFile);
            for (int i = 0; i < 52; i++)
            {
                Letters[i] = lines[i];
            }
            for (int i = 52; i < 62; i++)
            {
                Digits[i - 52] = lines[i];
            }
            for (int i = 62; i < 72; i++)
            {
                Operators[i - 62] = lines[i];
                System.Console.WriteLine(Operators[i - 62]);
            }
            for (int i = 72; i < 83; i++)
            {
                Separators[i - 72] = lines[i];
                System.Console.WriteLine(Separators[i - 72]);
            }
            int a;

        }
    }
}