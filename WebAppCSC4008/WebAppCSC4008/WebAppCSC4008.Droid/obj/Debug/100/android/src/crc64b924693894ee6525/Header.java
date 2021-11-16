package crc64b924693894ee6525;


public class Header
	extends crc64a5a37c43dff01024.UserControl
	implements
		mono.android.IGCUserPeer
{
/** @hide */
	public static final String __md_methods;
	static {
		__md_methods = 
			"";
		mono.android.Runtime.register ("WebAppCSC4008.Header, WebAppCSC4008.Droid", Header.class, __md_methods);
	}


	public Header (android.content.Context p0)
	{
		super (p0);
		if (getClass () == Header.class)
			mono.android.TypeManager.Activate ("WebAppCSC4008.Header, WebAppCSC4008.Droid", "Android.Content.Context, Mono.Android", this, new java.lang.Object[] { p0 });
	}

	private java.util.ArrayList refList;
	public void monodroidAddReference (java.lang.Object obj)
	{
		if (refList == null)
			refList = new java.util.ArrayList ();
		refList.add (obj);
	}

	public void monodroidClearReferences ()
	{
		if (refList != null)
			refList.clear ();
	}
}
