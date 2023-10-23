using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Lab_2.HashTable
{
    public class Node<T>
    {
        public Node()
        {
            Key = default!;
            Value = string.Empty;
        }
        public T Key { get; set; }
        public string Value { get; set; }

    }
}