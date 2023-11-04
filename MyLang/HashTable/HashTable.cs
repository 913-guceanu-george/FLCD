namespace MyLang.HashTable
{
    public class HashTable<Key>
    {
        public HashTable()
        {
            Elements = new Node<Key>[HashSize];
            for (int i = 0; i < HashSize; i++)
            {
                Elements[i] = new();
            }
        }

        private int HashSize { get; set; } = 20;
        private Node<Key>[] Elements { get; set; }

        private int HashFunc(Key key)
        {
            int hash = key!.GetHashCode();
            return ((hash >= 0) ? hash : -hash) % HashSize;
        }

        private bool IsKeyValid(Key key)
        {
            int index = HashFunc(key);
            return Elements.ElementAt(index)!.Value.Equals(string.Empty);
        }

        public void Add(Key key, String val)
        {
            while (!IsKeyValid(key))
            {
                int oldSize = HashSize;
                HashSize += 10;
                Node<Key>[] newElems = new Node<Key>[HashSize];
                for (int i = 0; i < oldSize; i++)
                {
                    newElems[i] = Elements[i];
                }
                for (int i = oldSize; i < HashSize; i++)
                {
                    newElems[i] = new();
                }
                Elements = newElems;
            }

            int index = HashFunc(key);
            Elements[index] = new() { Key = key, Value = val };
        }

        public string Get(Key key)
        {
            int index = HashFunc(key);
            return Elements[index].Value;
        }

        public Key GetKey(String val)
        {
            for (int i = 0; i < HashSize; i++)
            {
                if (Elements[i].Value.Equals(val))
                {
                    return Elements[i].Key;
                }
            }
            return default!;
        }


        public void Remove(Key key)
        {
            int index = HashFunc(key);
            Elements[index] = new();
        }

        public void Clear()
        {
            Elements = new Node<Key>[HashSize];
            for (int i = 0; i < HashSize; i++)
            {
                Elements[i] = new();
            }
        }

        public bool Contains(Key key)
        {
            int index = HashFunc(key);
            return Elements[index].Key!.Equals(string.Empty);
        }

        public int Count()
        {
            int count = 0;
            foreach (Node<Key> element in Elements)
            {
                if (!element.Value.Equals(string.Empty))
                {
                    count++;
                }
            }
            return count;
        }
    }
}