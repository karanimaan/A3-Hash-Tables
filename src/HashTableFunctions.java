package src;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

class HashTableFunctions
{

   // hash function weights
   // 9 integers, each in the range 0-5 to act as weights for the characters in the keys
   int [] weights = new int[9];
   // ADD YOUR WEIGHTS INSTEAD OF 1s

   public HashTableFunctions() {
      try (BufferedReader reader = new BufferedReader(new FileReader("weights.txt"))) {
         for (int i = 0; i < weights.length; i++) {
            weights[i] = Integer.parseInt(reader.readLine());
         }
      }
      catch (IOException e) {
         e.printStackTrace();
      }
   }

   // returns True if the hash table contains string s
   // return False if the hash table does not contain string s
   boolean find ( String s, int h, int hashTableSize, String [] hashTableArray )
   {
      for (String element : hashTableArray) {
         if (element.equals(s)) {
            return true;
         }
      }
      return false;
   }
}
