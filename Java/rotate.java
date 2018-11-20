/*
Coded By : Medi W. Assumani
Language : JAVA
Problem: Write a function that rotates an array of size n by d elements
*/

public class Problem8{
  public static void main(String[]args){



  }
  /*
  Function to return an array of elements shifted by d. From d to array.lenght
  @param array : the list of integers
  @param n : the length of the array
  @param d: the number of elemntsto rotate by
  */
  public static int[] shiftRightElements(int []array, int n, int d){

    int [] shiftedArray = new int[array.length - d];
      for(int index = 0 ; index < shiftedArray.length; index++){
        shiftedArray[index] = array[d];
      }
      return shiftedArray;
  }
  /*
  Function to return an array of the unshifted elementsin the array
  @param array : the list of integers
  @param n : the length of the array
  @param d: the number of elemntsto rotate by
  */

  public static int[] unshiftedElements(int []array, int n, int d){

    int [] tempArray = new int[d];
      for(int index = 0; index < tempArray.length; index++){
        tempArray[index] = array[index];
      }
      return tempArray;
  }
}
