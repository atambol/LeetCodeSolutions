class Solution {
    public List<String> fullJustify(String[] words, int maxWidth) {
        List<String> sol = new ArrayList<String>();
        List<Literal> literals = new ArrayList<Literal>();
        Literal literal;
        int count = 0;
        for (String word: words) {
            // dont do anything if the first word just fits the maxWidth
            if (literals.size() == 0 && word.length() + 1 >= maxWidth) {
                ;
            }    
            
            // add literals to sol if the new word exceeds limits
            else if (count + 1 + word.length() > maxWidth) {
                pad(literals, maxWidth, count);
                sol.add(collate(literals));
                count = 0;
                literals.clear();
            }
            
            // if the new word is within limit, add a padding to the previous word
            else if (literals.size() > 0) {
                literal = literals.get(literals.size()-1);
                literal.addOnePadding();
                count++;
            }
            
            // update character count and add the new word
            count += word.length();
            literals.add(new Literal(word));
        }
        
        // add the final word with left justification
        literal = literals.get(literals.size()-1);
        while (count < maxWidth) {
            literal.addOnePadding();
            count++;
        }
        sol.add(collate(literals));
        
        return sol;
    }
    
    // add correct padding to the literals based on maxWidth
    public void pad(List<Literal> literals, int maxWidth, int count) {
        Literal literal;
        if (literals.size() > 1) {
            while (count < maxWidth) {
                for (int i = 0; i < literals.size() - 1; i++) {
                    literal = literals.get(i);
                    literal.addOnePadding();
                    count++;

                    if (count == maxWidth) {
                        break;
                    }
                }
            }
        } else {
            literal = literals.get(literals.size()-1);
            while (count < maxWidth) {
                literal.addOnePadding();
                count++;
            }
        }
    }
    
    // join all the literals and create a sentence
    public String collate(List<Literal> literals) {
        Literal literal;
        String[] sentence = new String[literals.size()];
        for (int i = 0; i < literals.size(); i++) {
            literal = literals.get(i);
            sentence[i] = literal.stringify();
        }
        return String.join("", sentence);
    }
    
    // represent the word as an object with text and padding
    class Literal {
        private String text;
        private int padCount;
        
        public Literal(String text) {
            padCount = 0;
            this.text = text;
        }
        
        public String stringify() {
            String spaces = new String(new char[padCount]).replace('\0', ' ');
            return text + "" + spaces;
        }
        
        public void addOnePadding() {
            padCount++;
        }
    }
    
}
