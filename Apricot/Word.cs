﻿using System;
using System.Collections.ObjectModel;

namespace Apricot
{
    public class Word
    {
        private string name = null;
        private Collection<string> attributeCollection = null;

        public string Name
        {
            get
            {
                return this.name;
            }
            set
            {
                this.name = value;
            }
        }

        public bool HasAttributes
        {
            get
            {
                return this.attributeCollection.Count > 0;
            }
        }

        public Collection<string> Attributes
        {
            get
            {
                return this.attributeCollection;
            }
            set
            {
                this.attributeCollection = value;
            }
        }

        public Word()
        {
            this.attributeCollection = new Collection<string>();
        }
    }
}
